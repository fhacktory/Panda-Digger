$(document).ready(function() {
    $("#playlist").on("click", "tr", function(event) {
        $.ajax({
            dataType: "json",
            url: "play/" + $(event.currentTarget).index(),
        });
    });
});

(function worker_new() {
    $.ajax({
        dataType: "json",
        url: "new/" + $("#playlist tr").length,
        success: function(data) {
            $.each(data.new, function(index, value){
                $("#playlist").append("<tr><td>" + value + "</td></tr>");
            });
        },
        complete: function() {
            setTimeout(worker_new, 10000);
        }
    });
})();

(function worker_pos() {
    $.ajax({
        dataType: "json",
        url: "pos",
        success: function(data) {
                <!-- $("#pos").html(data.pos); -->
                $("#playlist td").css("font-weight", "normal");
            $("#playlist tr:nth-child(" + (data.pos + 1) + ") td").css("font-weight", "bold");
        },
        complete: function() {
            setTimeout(worker_pos, 1000);
        }
    });
})();
