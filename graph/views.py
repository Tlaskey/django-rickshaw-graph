# Copyright (c) 2014 Tyler Laskey
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from django.http import HttpResponse
import json
import time
import math
import random


def index(request):
    return HttpResponse('''
    <html><head>
  <meta http-equiv="content-type" content="text/html; charset=UTF-8">
  <title> - jsFiddle demo by tlaskey</title>
  
  <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
  
  
  
  
  <script type="text/javascript" src="http://code.jquery.com/ui/1.8.18/jquery-ui.min.js"></script>
  
  
  <link rel="stylesheet" type="text/css" href="/css/result-light.css">
  
    
      <link rel="stylesheet" type="text/css" href="http://code.shutterstock.com/rickshaw/examples/css/lines.css">
    
  
    
      <link rel="stylesheet" type="text/css" href="http://code.shutterstock.com/rickshaw/src/css/graph.css">
    
  
    
      <script type="text/javascript" src="http://code.shutterstock.com/rickshaw/vendor/d3.min.js"></script>
    
  
    
      <script type="text/javascript" src="http://code.shutterstock.com/rickshaw/vendor/d3.layout.min.js"></script>
    
  
    
      <script type="text/javascript" src="http://code.shutterstock.com/rickshaw/rickshaw.js"></script>
    
  
    
      <link rel="stylesheet" type="text/css" href="https://raw.githubusercontent.com/shutterstock/rickshaw/master/src/css/legend.css">
    
  
  <style type="text/css">
    #chart_container {
        position: relative;
        display: inline-block;
        font-family: Arial, Helvetica, sans-serif;
}
#chart {
        display: inline-block;
        margin-left: 40px;
}
#y_axis {
        position: absolute;
        top: 0;
        bottom: 0;
        width: 40px;
}
#legend {
        display: inline-block;
        vertical-align: top;
        margin: 0 0 0 10px;
}
#x_axis {
    position:absolute;
}
  </style>
  


<script type="text/javascript">//<![CDATA[ 
$(window).load(function(){
var seriesData = [
    [],
    [],
    [],
    []
];

var now = new Date().getTime()/1000;
now = Math.floor(now);
for (var t = now - 3600; t < now; t += 60) {
    for (var s = 0; s < seriesData.length; s++) {
        var new_Array = {x: t, y: Math.floor(Math.random()*100+1)};
        seriesData[s].push(new_Array);
                           }
}

var ajaxGraph = new Rickshaw.Graph.Ajax( {
        element: document.querySelector("#chart"),
        stroke: true,
        width: 550,
        height: 250,
        dataURL: '/graph/data'
} );

var time = new Rickshaw.Fixtures.Time();
var minutes = time.unit('15 minute');

var x_axis = new Rickshaw.Graph.Axis.Time({
    graph: graph,
    timeUnit: minutes,
    element: document.getElementById('x_axis')
});

var y_axis = new Rickshaw.Graph.Axis.Y( {
        graph: graph,
        orientation: 'left',
        tickFormat: Rickshaw.Fixtures.Number.formatKMBT,
        element: document.getElementById('y_axis')
} );
var times = new Rickshaw.Fixtures.Time();
var minute = times.unit('15 minute');
var hoverDetail = new Rickshaw.Graph.HoverDetail( {
    element: document.querySelector('hover'),
    graph: graph,
    xFormatter: function(epoch) {
        var utcSeconds = new Date().getTime()/1000;
        var d = new Date(0);
        d.setUTCSeconds(utcSeconds);
        return d; },
    yFormatter: function(y) { return Math.floor(y) + " percent"; }
} );

var legend = new Rickshaw.Graph.Legend( {
        element: document.querySelector('#legend'),
        graph: graph
} );

graph.render();
});//]]>  

</script>


</head>
<body>
  
    
<div id="chart_container">
        <div id="y_axis"></div>
        <div id="chart" class="rickshaw_graph"></div>
        <div id="x_axis"></div>
</div>
<div id="legend" class="rickshaw_legend"></div>
    <div id="hover"></div>
  





</body></html>
    
    
    ''')
    
def data(request):
    seriesData = [[],[],[],[]]
    epoch_time = int(time.time())
    for t in range(epoch_time-3600, epoch_time, 60):
        for s in range(0, len(seriesData)):
            new_list = {"x": t,"y" :math.floor(random.randint(0,11))}
            seriesData[s].append(new_list)
    seriesInfo =  [{
            " name": "Idle",
             "data": seriesData[0],
            "color":'#ff0000'
        }, {
             "name": "I/O",
             "data": seriesData[1],
            "color": '#0000ff'
        }, {
             "name": "System",
             "data": seriesData[2],
            "color": '#00FF00'
        }, {
            "name": "User",
            "data": seriesData[3],
           "color": "#FF00FF"
        }]
    seriesInfo = json.dumps(seriesInfo)
    return HttpResponse(seriesInfo)