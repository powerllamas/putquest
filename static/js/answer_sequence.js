$(document).ready(function(){

	$("#formset").before("<p>Aby zmienić kolejność odpowiedzi, przeciągnij je używając uchwytu po lewej stronie. Nie zapomnij <b>zapisać</b> zmian.</p>");
	$("#formset thead").children().prepend("<td></td>");
	$("#formset thead").children().each(function() {
		$(this).children().eq(2).hide();
	});

	var itemsContainer = $("#formset tbody");
	itemsContainer.children().prepend("<td class='handle'></td>");
	itemsContainer.children().each(function() {
		$(this).children().eq(2).hide();
	});

	itemsContainer.sortable({
		cursor: 'move',
		axis: 'y',
		handle: 'td.handle',
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
