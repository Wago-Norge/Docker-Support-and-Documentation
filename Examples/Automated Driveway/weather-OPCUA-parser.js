var items = new Array(4);
var values = new Array(4);
values[0] = msg.temp;
values[1] = String(msg.rain);
values[2] = msg.rainType;
values[3] = msg.ice;

items[0] = 
{
    name: "Hour"+String(msg.hour)+".temp",
    nodeId: "ns=4;s=|var|PFC200_IoT.Application.PLC_PRG.hour"+String(msg.hour)+".temp",
    datatypeName: "Int16"
}
items[1] =
{
    name: "Hour"+String(msg.hour)+".rain",
    nodeId: "ns=4;s=|var|PFC200_IoT.Application.PLC_PRG.hour"+String(msg.hour)+".rain",
    datatypeName: "Float"
}
items[2] = 
{
    name: "Hour"+String(msg.hour)+".rainType",
    nodeId: "ns=4;s=|var|PFC200_IoT.Application.PLC_PRG.hour"+String(msg.hour)+".rainType",
    datatypeName: "String"
},
items[3] =
{
    name: "Hour"+String(msg.hour)+".ice",
    nodeId: "ns=4;s=|var|PFC200_IoT.Application.PLC_PRG.hour"+String(msg.hour)+".ice",
    datatypeName: "Boolean"
}

msg = {
    payload: {
        hour: msg.hour,
        temp: msg.temp,//msg.temp,
        rain: msg.rain,
        rainType: msg.rainType,
        ice: msg.ice
    },
    nodetype: "node",
    injectType: "write",
    addressSpaceItems: items,
    valuesToWrite: values,
    topic: "",
    _msgid: msg._msgid
}
return msg;