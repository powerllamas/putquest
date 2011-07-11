$(document).ready(function(){
    $("table.stats").each(function(index) {
        var placeholder = $('<div class="graph"><div id="graph'+index+'"></div></div>');
        placeholder.insertAfter(this);
        var graph = $("#graph"+index);
        graph.height(200);
        graph.width(placeholder.width());
        $(window).resize(function() {
            var newWidth = function(ref) {
                return ref.width();
            }(placeholder);
            graph.width(newWidth);
        });
        $(this).hide();
        var data = [];
        $(this).find("tbody tr").each(function() {
            var data_row = $(this).children();
            var value = parseInt(data_row.eq(1).text(), 10);
            var label = data_row.eq(0).text()+ ' ('+ value + ' odpowiedzi)';
            var serie = function(label, value) {
                var val = {};
                val.label = label;
                val.data = value;
                return val;
            }(label, value);
            data.push(serie);
        });
        $.plot(graph, data, 
            {
                series: {
                    pie: {
                        show: true,
                        label: {
                            show: true,
                            formatter: function(label, series) {
                                return Math.round(series.percent)+'%';
                            }
                        }
                    }
                }
            }
        );
    });
});
