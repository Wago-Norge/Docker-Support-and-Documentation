var numberOfHours = 3;
var i = 0;
var forecasts = new Array(numberOfHours); //Array consisting of imminent forecasts, hour by hour
//Symbol list from YR - every precipitation category
var yrSymbols = new Array("12", "13", "14", "23", "31", "32", "33", "34", "47", "48", "49", "50", "42d", "07d", "43d", "44d", "08d", "45d", "26d", "20d", "27d", "28d", "21d", "29d", "42n", "07n", "43n", "44n", "08n", "45n", "26n", "20n", "27n", "28n", "21n", "29n", "42m", "07m", "43m", "44m", "08m", "45m", "26m", "20m", "27m", "28m", "21m", "29m");


//void fillHour(j);
function fillHour(i){
    forecasts[i].hour = i+1;
    forecasts[i].temp = msg.payload.weatherdata.forecast[0].tabular[0].time[i].temperature[0].$.value;
    forecasts[i].rain = msg.payload.weatherdata.forecast[0].tabular[0].time[i].precipitation[0].$.value;
    forecasts[i].rainType = msg.payload.weatherdata.forecast[0].tabular[0].time[i].symbol[0].$.number;
    
    for (var k = 0; k < yrSymbols.length; k++){
        if(forecasts[i].rainType === yrSymbols[k]){
            forecasts[i].rainType = "snow inbound";
        }
    }
    if(forecasts[i].rainType != "snow inbound") forecasts[i].rainType = "no snow";
    
}

for (i = 0; i < numberOfHours; i++){
    //Format every forecast object
    forecasts[i] = {
        hour: 0,
        temp: 0,
        rain: 0,
        rainType: "no snow",
        ice: false
    }
    //Fill forecast with information
    fillHour(i);
}



//Puts every forecast into
msg.payload = forecasts;

return [forecasts[0], forecasts[1], forecasts[2]];