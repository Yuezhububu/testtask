function taskCheck() {
  $('.checked').click(function(event) {
    var checkedId = $(this).closest("form")[0].id;
    $.ajax({
      url : "/task/checktask/",
      type : "POST",
      data : $('#' + checkedId).serialize(),
      success : function(html) {},
      error : function(xhr, msg, err) {
        alert(err + ": failed checking task.");
        // Reload page to avoid inconsistent state with UI and database.
        location.reload(true);
      }
    });
  });
}

taskCheck();

$('#newTaskForm').on('submit', function(event) {
    event.preventDefault();
    $.ajax({
        url : "/task/newtaskform/",
        type : "POST",
        data : $('#newTaskForm').serialize(),
        success : function(html) {
          // Update task list with new task.
          $('#taskListTable').html(html);
          // Add checkbox event handler to new task.
          taskCheck();
          // Clear form.
          $('#new_task_title').val('');
          $('#new_description').val('');
        },
        error : function(xhr, msg, err) {
          $('#new-task-error').text(err + ": failed creating task.");
        }
    });
});
