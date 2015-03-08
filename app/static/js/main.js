/**
 * Created by phrayezzen on 10/7/14.
 */

var addResult = function(result) {
  var contacts = result["result"];
  for (var i = 0; i < contacts.length; i++) {
    var contact = contacts[i];
    for (var field in contact) {
      if (contact.hasOwnProperty(field) && contact[field] === null) {
        contact[field] = "";
      }
    }

    $("tbody").append("<tr id='" + contact["contactId"] + "'>" +
      "<td>" + contact["firstName"] + " " + contact["lastName"] + "</td>" +
      "<td>" + contact["phone"] + "</td>" +
      "<td>" + contact["address"] + "</td>" +
      "<td>" + contact["city"] + "</td>" +
      "<td>" + contact["state"] + "</td>" +
      "<td>" + contact["zip"] + "</td>" +
      "<td><button class='delete-btn btn btn-warning btn-xs'>Delete Contact</button></td>" +
      "</tr>");
  }
};

$(document).ready(function() {
  $.getJSON("/contact", addResult);

  $("#add").on("click", function() {
    $.post("/contact", $("form").serialize(), addResult);
  });

  $("tbody").on("click", ".delete-btn", function() {
    var deleteId = $(this).closest("tr").attr("id");
    $(this).closest("tr").remove();

      $.ajax({
          url: "/contact/" + deleteId,
          type: "DELETE:"
      });

  });
});