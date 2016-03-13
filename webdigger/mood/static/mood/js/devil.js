$(document).ready(function() {
    $("#playlist").on("click", "tr", function(event) {
        $.ajax({
            dataType: "json",
            url: "play/" + $(event.currentTarget).index(),
        });
        $('html, body').animate({
            scrollTop: $(event.currentTarget).offset().top
        }, 2000);
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
            if (data.new.length > 0)
            {
                var last_index = $("#playlist tr:last-child").index();
                var last_prev = $("#playlist tr:nth-child(" + last_index + ") td");
                if (last_prev.css("font-weight") === "bold")
                {
                    $('html, body').animate({
                        scrollTop: last_prev.offset().top
                    }, 2000);
                }
            }
        },
        complete: function() {
            setTimeout(worker_new, 5000);
        }
    });
})();

(function worker_pos() {
    $.ajax({
        dataType: "json",
        url: "pos",
        success: function(data) {
                $("#playlist td").css("font-weight", "normal");
            $("#playlist tr:nth-child(" + (data.pos + 1) + ") td").css("font-weight", "bold");
        },
        complete: function() {
            setTimeout(worker_pos, 1000);
        }
    });
})();
