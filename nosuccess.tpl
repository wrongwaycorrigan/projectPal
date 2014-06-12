<!DOCTYPE html>
<html>
<head>
<title>Project Pal</title>
<link rel="stylesheet" type="text/css" href="/static/style.css">
</head>
<body>
<img src="/static/images/projectpal.png" height="200" width="220"><br>
<p>
Sorry, {{ project_name }} was not created properly. Please contact your systems administrator.
<p>
<p>Existing Projects:
    %for proj in projects:
        <li>{{ proj }}</li>
    %end
</p>
<form method="GET" action="/">
<button class="button" type="submit">
      Back to Create New Project
</button>
</form>
</body>

</html> 
