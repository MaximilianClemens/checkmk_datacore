#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

metric_info["bytesallocated"] = {
    "title" : _("Allocated"),
    "color": "#4682b4",
    "unit" : "bytes",
}

metric_info["bytestotal"] = {
    "title" : _("Total"),
    "color": "#ff1515",
    "unit" : "bytes",
}

metric_info["bytesavailable"] = {
    "title" : _("Available"),
    "color": "#bebebe",
    "unit" : "bytes",
}

metric_info["bytesinreclamation"] = {
    "title" : _("InReclamation"),
    "color": "#ffce00",
    "unit" : "bytes",
}

metric_info["bytesoversubscribed"] = {
    "title" : _("OverSubscribed"),
    "color": "#000000",
    "unit" : "bytes",
}

metric_info["maxwritetime"] = {
    "title" : _("MaxWriteTime"),
    "color": "#4db7b7",
    "unit" : "s",
}

metric_info["maxreadtime"] = {
    "title" : _("MaxReadTime"),
    "color": "#47a85a",
    "unit" : "s",
}

#metric_info["totalbyteswritten"] = {
#    "title" : _("totalbyteswritten"),
#    "color": "#4db7b8",
#    "unit" : "bytes/s",
#}
#
#metric_info["totalbytesread"] = {
#    "title" : _("totalbytesread"),
#    "color": "#47a85b",
#    "unit" : "bytes/s",
#}


graph_info["datacore_pool_usage"] = {
    "title"   : _("Pool Usage"),
    #"legend_scale": GB,
    #"legend_precision": 0,
    "metrics" : [
        ( "bytesallocated", "area" ),
        ( "bytesinreclamation", "stack" ),
        ( "bytesavailable", "stack" ),
        ( "bytesoversubscribed", "stack" ),
        ( "bytestotal", "line" ),
    ],
}

graph_info["datacore_pool_latency"] = {
    "title"   : _("Pool Latency"),
    #"legend_scale": m,
    #"legend_precision": 3,
    "metrics" : [
        ( "maxwritetime", "area" ),
        ( "maxreadtime", "-area" )
    ],
}

#graph_info["datacore_pool_io"] = {
#    "title"   : _("Pool IO"),
#    "metrics" : [
#        ( "totalbyteswritten", "area" ),
#        ( "totalbytesread", "-area" )
#    ],
#}