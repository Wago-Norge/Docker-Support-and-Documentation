//Subscribing can be used to retrieve values, status and commands from somewhere/something else.

(* -----------------DECLARATION----------------- *)

	fbSubscribe	: WagoAppCloud.FbSubscribeMQTT;
    topic           : STRING := 'ID/MACID/commands';
	status			: WagoSysErrorBase.FbResult;
	parserJSON		: WagoAppJSON.Fb_JSON_ParseAndModify;
	jsonGet			: ARRAY [0..10] OF WagoAppJSON.typJSON_Pointer;
	trigger			: BOOL := FALSE;
    getTrigger      : BOOL;
	parseTrigger	: BOOL;
    subDataReceived : BOOL;

	buffer			: ARRAY [0..255] OF BYTE;
	size			: DWORD;
	
	receivedStr		: STRING;
    statusStr       : STRING;
	parsed_json		: STRING(JSON_MAX_STRING);
	receivedTopic	: STRING;
    errorCount		: SINT;

    (* TIP *)
    //You can retrieve MAC ID with fb := WagoAppConfigTool.FbGetX1_ActualNetworkAddress -> macID := fb.sMacAddress.
    //Thereafter you can use the MAC ID to publish/subscribe to a unique topic:
    //Use WagoAppString to concatenate string together. Concatenate / + macid + /data for a unique topic.
(* --------------END DECLARATION-------------- *)

(* ------------------PROGRAM------------------ *)

//Settings for subscription
fbSubscribe(
	xSubscribe:= TRUE, 
	sTopic:= topic, 
	eQoS:= eQualityOfService.QoS0, 
	aPayloadData:= buffer, 
	xBusy=> , 
	xError=> , 
	oStatus=> status, 
	xDataReceived=> subDataReceived, 
	dwRxNBytes=> , 
	xDataTruncated=> , 
	sReceivedTopic=> receivedTopic);
IF subDataReceived THEN
	statusStr := 'Received';
	errorCount := 0;
ELSE IF NOT (statusStr = 'Received') THEN
		errorCount := errorCount + 1;
		IF errorCount > 3 THEN
			statusStr := 'Failed';
		END_IF
	 END_IF
END_IF

parseTrigger := TRUE;
parserJSON(
	pData:= ADR(buffer), 
	udiSizeData:= SIZEOF(buffer), 
	oStatus=> , 
	xError=> , 
	xDone=> , 
	diToken=> , 
	xTrigger:= parseTrigger);

//Store incoming values in an array of JSON objects:
getTrigger := TRUE;
jsonGet[0] := parserJSON.GetValueByPath(sPointer:= '/Value_1', xTrigger:= getTrigger);
getTrigger := TRUE;
jsonGet[1] := parserJSON.GetValueByPath(sPointer:= '/Value_2', xTrigger:= getTrigger);
getTrigger := TRUE;
jsonGet[2] := parserJSON.GetValueByPath(sPointer:= '/Value_3', xTrigger:= getTrigger);
getTrigger := TRUE;
jsonGet[3] := parserJSON.GetValueByPath(sPointer:= '/Random_Value_Like_Temperature_Or_Voltage_Etc', xTrigger:= getTrigger);

receivedStr := WagoAppString.Mem_to_PrintableString(pData:= ADR(buffer), udiDataSize:= SIZEOF(buffer));
(* The received message would look something like this: 
    {   
        "Value_1": "123.4,
    	"Value_2": "234.56",
    	"Value_3": "345.678",
    	"Random_Value_Like_Temperature_Or_Voltage_Etc": "1337"
    }'
*)

(* ----------------END PROGRAM---------------- *)