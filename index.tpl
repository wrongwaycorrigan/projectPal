<!DOCTYPE html>
<html>
<head>
<title>Project Pal</title>
<link rel="stylesheet" type="text/css" href="static/style.css">
</head>
<body>
<img src="/static/images/projectpal.png" height="200" width="220"><br>
<p>
Project Name
<form method="POST" action="/submitproject">
    <input name="project_name" id="textbox" type="text" />
<p>
Destination
<div class="selectbox">
    <select name="destination">
		<option value="local">Local Machine</option>
		<option value="zeus">Zeus</option>
		<option value="atlas">Atlas</option>
	</select>
<p>
Preset
<div class="selectbox">
    <select name="project_type">
		<option value="hdtv_1080_24">HDTV 1080 24</option>
		<option value="hdtv_1080_25">HDTV 1080 25</option>
		<option value="hdtv_1080_2997">HDTV 1080 29.97</option>
		<option value="hdtv_1080i_5994">HDTV 1080i 59.94</option>
		<option value="film_2k">Film 2K</option>
		<option value="film_4k">Film 4K</option>
		<option value="film_5k">Film 5K</option>
		<option value="ipad_retina">iPad Retina</option>
		<option value="stock">Stock</option>
    </select>
</div>
<p>
<button class="button" type="submit">
      Create New Project
</button>
<p>
<div class="projects">
	<div class="h1">Current Projects</div>
    <p>
    %for proj in projects:
        <li><a href='/shot/{{ proj }}'>{{ proj }}</a></li>
    %end
    </p>
</div>
</form>

</body>

</html> 
