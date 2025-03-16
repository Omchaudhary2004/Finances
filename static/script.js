$(document).ready(function() {
    $('#runScript').click(function() {
        // Get input values
        const input1 = $('#input1').val();
        const input2 = $('#input2').val();
        
        // Show loading indicator
        $('#result').html('Running script...');
        
        // Make AJAX call to Django view with input parameters
        $.ajax({
            url: '{% url "run_script" %}',
            type: 'GET',
            data: {
                'input1': input1,
                'input2': input2
            },
            success: function(data) {
                // Display the result
                $('#result').html('Result: ' + data.result);
            },
            error: function(xhr, status, error) {
                $('#result').html('Error: ' + error);
            }
        });
    });
});