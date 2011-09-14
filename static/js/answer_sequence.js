$(document).ready(function(){
	var itemsContainer = $("#formset tbody");
	$("#formset thead").children().prepend("<td></td>");
	itemsContainer.children().prepend("<td class='handle'></td>");
	itemsContainer.sortable({
		cursor: 'move',
		axis: 'y',
		update: function(event, ui) {
			itemsContainer.children().each(function(index) {
				var answerContentInput = $(this).children().eq(1).children().eq(2);
				var answerContent = answerContentInput.attr("value");
				if ($.trim(answerContent) != "") {
					var sequenceInput = $(this).children().eq(2).children().eq(0);
					sequenceInput.attr("value", index);
				};
			});
		}
	});
});
