PROGRAM PLC_PRG
VAR
	incomingRain : REAL;
	tempIn : INT;
	tempOut : INT;
	forecastTemp : INT;
	forecastRain : REAL;

	xEnableManual : BOOL := FALSE;
	xEnableAuto : BOOL := FALSE;
	autoOn : BOOL;
	heatOn : BOOL;
	exception : BOOL;

	preTime : TIME := T#4H;   		//Predefined time for manual heating
	autoTime : TIME := T#90M; 		//Predefined time for when heating will start before snow/ice
	onTime : TIME;
	offTime : TIME;

	hour1 : WeatherData;
	hour2 : WeatherData;
	hour3 : WeatherData;
	hour4 : WeatherData;

	run : BOOL;
	manual1 : BOOL := FALSE;
	manual2 : BOOL := FALSE;
	manual3 : BOOL := FALSE;
	manual4 : BOOL := FALSE;
	enable1 : BOOL := TRUE;
	enable2 : BOOL := TRUE;
	enable3 : BOOL := TRUE;
	enable4 : BOOL := TRUE;
	auto1 : BOOL := TRUE;
	auto2 : BOOL := TRUE;
	auto3 : BOOL := TRUE;
	auto4 : BOOL := TRUE;
	mode1 : SINT := 3;
	mode2 : SINT := 3;
	mode3 : SINT := 3;
	mode4 : SINT := 3;

	auto: TOF;
	manTON: TON;
	manTON1: TON;
	manTON2: TON;
	manTON3: TON;
	manTON4: TON;
	F_TRIG_1: F_TRIG;
	F_TRIG_2: F_TRIG;
	F_TRIG_3: F_TRIG;
	F_TRIG_4: F_TRIG;
	F_TRIG_5: F_TRIG;
	timer1: WagoAppBuildingHVAC.FbOperatingHours_01;
	timer2: WagoAppBuildingHVAC.FbOperatingHours_01;
	timer3: WagoAppBuildingHVAC.FbOperatingHours_01;
	timer4: WagoAppBuildingHVAC.FbOperatingHours_01;
	charger_timer: WagoAppBuildingHVAC.FbOperatingHours_01;
	charger_powerMeasure: WagoAppPowerMeasurement.FbAC_Values_494;
	charger_powerTime: WagoAppBuildingHVAC.FbOperatingHours_01;

	powerMeter: BASIC.METER;
	reset_charger: BOOL;

END_VAR
VAR RETAIN PERSISTENT
	time1 : DWORD;
	time2 : DWORD;
	time3 : DWORD;
	time4 : DWORD;
	timeMin1 : DWORD;
	timeMin2 : DWORD;
	timeMin3 : DWORD;
	timeMin4 : DWORD;
	timeMin_charger: DWORD;
	kWh1 : REAL;
	kWh2 : REAL;
	kWh3 : REAL;
	kWh4 : REAL;
	kWh_charger: REAL;
	kWhTotal : REAL;
END_VAR
