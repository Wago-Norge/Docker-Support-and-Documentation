(*
This program is based on the WagoApp_1.6.1.x_Cloud_FbCollectionLogger_Example_01 in E!Cockpit.
It has however been edited for demonstrational purposes.
 *)

(* DECLARATION AND INITIAL VALUES *)


(* Purpose of the example program: 
FbCollectionLogger will sample 3 collections in different modes.
- Collection 1: EQUALLY_SPACED_COLLECTION_SAMPLES
- Collection 2: UNEQUALLY_SPACED_CUSTOMIZED_SAMPLES
- Collection 3: LIBRARY_DEFAULT_AUTOMATIC
*)
PROGRAM PLC_PRG
VAR RETAIN
	(* Sample and Publish intervals should be kept as retain *)
	(* Remanent variables *)
	tSampleInterval1 : TIME := T#3M;
	tPublishInterval1 : TIME := T#1S;
	tPublishInterval2 : TIME := T#200MS;
	tSampleInterval3 : TIME := T#60S;
	tPublishInterval3 : TIME := T#120S;
END_VAR

VAR
	(* Variables to be published to the cloud. *)
	tempInside	: WORD := 12;					//Temperature inside
	tempOutside	: WORD := 9;					//Temperature outside
	precipitation	: REAL := 0;				//Rain/Precipitation
	current		: REAL := 4.8;					//Current consumption
	powerAcc	: REAL := 113.4;				//Accumulated power /kWh
	powerHeat	: REAL := 40.1;					//kWh Heating
	powerCharg	: REAL := 73.3;					//kWh Charging
	status_charger	: STRING := 'charging';		//Status msg: 'charging'/'off'
	status_heating	: STRING := 'off';			//Status msg: 'heating'/'off'
	forecast		: STRING := 'cloudy';		//Weather type string
	switch			: BOOL	 := FALSE;			//On/off boolean for testing

	(* Define collections to categorize variables*)				//Can be just one collecation, if wanted.
	categories: ARRAY[0..2] OF WagoAppCloud.typCollection;

	(* Define the variables for the collections*)				//These will be inserted to categories
	category_Weather: ARRAY[0..2] OF WagoAppCloud.typVariableDescription;
	category_Power: ARRAY[0..2] OF WagoAppCloud.typVariableDescription;
	category_Strings: ARRAY[0..2] OF WagoAppCloud.typVariableDescription;
	
	oFbCollectionLogger: WagoAppCloud.FbCollectionLogger;		//Function block to export to cloud
	
	(* Timer *)
	xEnableTimer: BOOL := TRUE;
	tCyclicTimerSendTagCollection: TON;
	testSize : WORD;
	test2Size : INT;
	
END_VAR
(* _________________________________________________________________________________________________________*)
(* PROGRAM BELOW *)
(* Simulate changing values to transfer to the cloud *)
	powerCharg := powerCharg + 0.23*current;
	powerAcc := powerCharg + powerHeat;
	
	IF switch = FALSE THEN
		switch := TRUE;
	ELSE
		switch := FALSE;
	END_IF

    (* -------------------------------------------------------------------------------------------- *)
    (* Configuration of the collections and variables *)

	(* Refer to this for dwTypeId: 
	WORD = 
	REAL = 1
	BYTE = 3
	DWORD = 4
	BOOL = 5
	INT = 6
	UINT = 7
	STRING = 8
	*)
	 
	(* Init category 1 : Weather*)
	category_Weather[0].pAddress := ADR(tempInside);
	category_Weather[0].eValueType := WagoAppCloud.VVT_WORD;
	category_Weather[0].dwTypeId := 2;
	category_Weather[0].sTag := 'tempInside';
	category_Weather[0].sUnit := '°C';
	
	category_Weather[1].pAddress := ADR(tempOutside);
	category_Weather[1].eValueType := WagoAppCloud.VVT_WORD;
	category_Weather[1].dwTypeId := 2;
	category_Weather[1].sTag := 'tempOutside';
	category_Weather[1].sUnit := '°C';
	
	category_Weather[2].pAddress := ADR(precipitation);
	category_Weather[2].eValueType := WagoAppCloud.VVT_REAL;
	category_Weather[2].dwTypeId := 1;
	category_Weather[2].sTag := 'precipitation';
	category_Weather[2].sUnit := 'mm';
	
	(* Configuration of the collection. *)
	categories[0].dwCollectionId := 1;
	categories[0].sName := 'Weather';
	categories[0].pVariableDescriptions := ADR(category_Weather);
	categories[0].dwVariablesCount := 3;
	(* Configuration of the mode to sampling the data. 
	In this case all variables of category 1 will be send in equally spaced to the cloud. 
	The Trigger of a sample is set manual with the CollectionTrigger. *)
	categories[0].eSamplingDataMode := eSamplingMode.EQUALLY_SPACED_COLLECTION_SAMPLES;
	categories[0].pSampleInterval := ADR(tSampleInterval1);
	categories[0].pPublishInterval := ADR(tPublishInterval1);
    (* -------------------------------------------------------------------------------------------- *)

    (* -------------------------------------------------------------------------------------------- *)	
	(* Init category 2 : Power*)
	category_Power[0].pAddress := ADR(current);
	category_Power[0].eValueType := WagoAppCloud.VVT_REAL;
	category_Power[0].dwTypeId := 1;
	category_Power[0].sTag := 'Power_Consumption';
	category_Power[0].sUnit := 'kW';
	
	category_Power[1].pAddress := ADR(powerAcc);
	category_Power[1].eValueType := WagoAppCloud.VVT_REAL;
	category_Power[1].dwTypeId := 1;
	category_Power[1].sTag := 'Total_Power_Accumulated';
	category_Power[1].sUnit := 'kWh';

	category_Power[2].pAddress := ADR(powerHeat);
	category_Power[2].eValueType := WagoAppCloud.VVT_REAL;
	category_Power[2].dwTypeId := 1;
	category_Power[2].sTag := 'Heating';
	category_Power[2].sUnit := 'kWh';
	
	category_Power[3].pAddress := ADR(powerCharg);
	category_Power[3].eValueType := WagoAppCloud.VVT_REAL;
	category_Power[3].dwTypeId := 1;
	category_Power[3].sTag := 'Charging';
	category_Power[3].sUnit := 'kWh';

	(* Configuration of the collection. *)
	categories[1].dwCollectionId := 2;
	categories[1].sName := 'Power';
	categories[1].pVariableDescriptions := ADR(category_Power);
	categories[1].dwVariablesCount := 4;
	(* Configuration of the mode to sampling the data. 
	In this case at least one variable of collection 2 will be send irregularly to the cloud. 
	The Trigger of a sample is set manual with the CollectionTrigger or the VariableTrigger. *)
	categories[1].eSamplingDataMode := eSamplingMode.UNEQUALLY_SPACED_CUSTOMIZED_SAMPLES;
	categories[1].pPublishInterval := ADR(tPublishInterval2);
    (* -------------------------------------------------------------------------------------------- *)	


    (* -------------------------------------------------------------------------------------------- *)
	(* Init category 3 : Status : Cyclic*)
	category_Status[0].pAddress := ADR(status_charger);
	category_Status[0].eValueType := WagoAppCloud.VVT_STRING;
	category_Status[0].dwTypeId := 8;
	category_Status[0].sTag := 'Status_Charger';
	category_Status[0].sUnit := 'msg';
	
	category_Status[1].pAddress := ADR(status_heating);
	category_Status[1].eValueType := WagoAppCloud.VVT_STRING;
	category_Status[1].dwTypeId := 8;
	category_Status[1].sTag := 'Status_Heating';
	category_Status[1].sUnit := 'msg';
	
	category_Status[2].pAddress := ADR(forecast);
	category_Status[2].eValueType := WagoAppCloud.VVT_STRING;
	category_Status[2].dwTypeId := 8;
	category_Status[2].sTag := 'Forecast';
	category_Status[2].sUnit := 'msg';
	
	category_Status[3].pAddress := ADR(switch);
	category_Status[3].eValueType := WagoAppCloud.VVT_BOOL;
	category_Status[3].dwTypeId := 5;
	category_Status[3].sTag := 'testBool';
	category_Status[3].sUnit := 'Bool';
	
	(* Category 3 : Status *)
	categories[2].dwCollectionId := 3;
	categories[2].sName := 'Status_Messages';
	(* Configuration of the mode to sampling the data. 
	In this case the samples of collection 3 will be set automatically. The space between two timestamps are defined in the sample interval. *)
	categories[2].eSamplingDataMode := eSamplingMode.LIBRARY_DEFAULT_AUTOMATIC; // LIBRARY_DEFAULT_AUTOMATIC is the default mode
	categories[2].pPublishInterval := ADR(tPublishInterval3);
	categories[2].pSampleInterval := ADR(tSampleInterval3);
	categories[2].pVariableDescriptions := ADR(category_Status);
	categories[2].dwVariablesCount := 4;
    (* -------------------------------------------------------------------------------------------- *)	
	

	

(* Example to set the event with a timer intervall - CollectionTrigger or VariableTrigger *)
	(* Set an event with an Timer to send the variables in an intervall to the cloud *)
	tCyclicTimerSendTagCollection(IN:= xEnableTimer, PT:= tSampleInterval1);
	IF tCyclicTimerSendTagCollection.Q THEN
		categories[0].xCollectionTrigger := TRUE;
		
		xEnableTimer := FALSE;
	ELSE
		xEnableTimer := TRUE;
	END_IF

	
oFbCollectionLogger(pCollections := ADR(categories), dwCollectionsCount := 3);