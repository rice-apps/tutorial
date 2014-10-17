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
      "<td><a href='#'>Delete</a></td>" +
      "</tr>");
  }
};

$(document).ready(function() {
  $.getJSON("/getContacts", addResult);

  $("#add").on("click", function() {
    $.post("/addContact", $("form").serialize(), addResult);
  });

  $("tbody").on("click", "a", function() {
    $.get("/deleteContact/" + $(this).closest("tr").attr("id"));
    $(this).closest("tr").remove();
  });
});