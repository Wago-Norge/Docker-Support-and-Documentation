(* -----------------DECLARATION----------------- *)
    publisher			: WagoAppCloud.FbPublishMQTT;
	generateJSON		: WagoAppJSON.Fb_JSON_Writer_01;
	generateTrig		: BOOL := FALSE;
	publishTrig			: BOOL := FALSE;
	payload				: ARRAY[0..255] OF BYTE;
	dwSize				: DWORD;
	
	(* JSON Setup for publishing *)
	publishStr 			: STRING(JSON_MAX_STRING) := '{ 
	"Verdi_1": "#Parameter",
	"Verdi_2": "#Parameter",
	"Verdi_3": "#Parameter",
	"Random_Value_Like_Temperature_Or_Voltage_Etc": "#Parameter"
	}';
	
	publishJSON			: STRING(JSON_MAX_STRING);						//Parsed string that will be published
	publishVals			: ARRAY[0..3] OF STRING := ['','','',''];	//Array of values to be published
	publishTopic		: STRING(255) := 'topic';					//Topic

    (* TIP *)
    //You can retrieve MAC ID with fb := WagoAppConfigTool.FbGetX1_ActualNetworkAddress -> macID := fb.sMacAddress.
    //Thereafter you can use the MAC ID to publish/subscribe to a unique topic:
    //Use WagoAppString to concatenate string together. Concatenate / + macid + /data for a unique topic.

(* --------------END DECLARATION-------------- *)

(* ------------------PROGRAM------------------ *)

(* Set values that should be published *) 
publishVals[0] := REAL_TO_STRING(GVL.var1);
publishVals[1] := REAL_TO_STRING(GVL.var2);
publishVals[2] := REAL_TO_STRING(GVL.var3);
publishVals[3] := REAL_TO_STRING(GVL.var4);


//Genererer JSON-string med verdiene vi la inn over. Erstatter #Parameter med verdiene.
//Generate JSON for publishing. Replaces "#Parameter" with the values in publishVals
generateTrig := TRUE;
generateJSON(
	sJSON_BaseFrame := publishStr,
	aParameterValues := publishVals,
	xTrigger := generateTrig,
	sOutput := publishJSON,
	xDone =>
);

dwSize := StrLength(sBuffer := publishJSON, udiSize:= 2000);
// dwSize := wagoappstring.length(publishJSON);

publishTrig := TRUE;
MemCopy(pDest := ADR(payload), pSource := ADR(publishJSON), udiSize := dwSize);
publisher(
	sTopic 		:= publishTopic,
	eQualityOfService := 1,
	xRetain 	:= TRUE,
	dwSize		:= dwSize,
	aData		:= payload,
	xTrigger	:= publishTrig,
	xBusy		:= ,
	xError		:= ,
	oStatus		:=
);
(* ----------------END PROGRAM---------------- *)

