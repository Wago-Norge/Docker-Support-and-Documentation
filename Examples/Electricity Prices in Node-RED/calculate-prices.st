(* 
    This program checks power consumption in kW every minute, and calculates a mean for the last hour. It then calculates the cost, based on the kWh price from Nordpool, from the last hour.
*)

timeComponents := WagoAppTime.FuGetLocalTimeComponents();
hour := timeComp.uiHour;                                    // Get hour integer
GVL.NOK_Current := GVL.intraday_prices[hour];               // Pick price for this hour

ton_timer(IN := TRUE);
IF ton_timer.Q THEN
	kW_Hourly := kW_Hourly + GVL.kW_Total;						    // Check kW every minute
	kW_Hourly_Heating := kW_Hourly_Heating + GVL.kW_Heating;
	kW_Hourly_Charging := kW_Hourly_Charging + GVL.kW_Charger;
	IF timeComp.uiMinute = 0 THEN							        // New hour started
		GVL.kW_Historical := kW_Hourly/60.0;
		GVL.historical_kWh[hour-1] := GVL.kW_Historical;						                            // Insert consumed kW/60.0 into array. Provides kWh with a per-minute resolution. 
		GVL.NOK_Total := GVL.NOK_Total + GVL.kW_Historical*GVL.intraday_prices[hour-1];			            // Total NOK last hour
		GVL.NOK_Tot_Heating := GVL.NOK_Tot_Heating + GVL.NOK_Tot_Heating*GVL.intraday_prices[hour-1];	    // Heating NOK last hour
		GVL.NOK_Tot_Charging := GVL.NOK_Tot_Charging + GVL.NOK_Tot_Charging*GVL.intraday_prices[hour-1];	// Charging NOK last hour
		// Reset
		kW_Hourly := 0;
		kW_Hourly_Heating := 0;
		kW_Hourly_Charging := 0;
	END_IF
	ton_timer(IN := FALSE);
END_IF