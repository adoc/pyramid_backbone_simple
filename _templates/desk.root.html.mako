<!doctype html>
<html>
    <head>
        <!-- Inspired by http://backbonetutorials.com/videos/beginner/ /-->
      %if self.title:
        <title>Backbone/Pyramid - ${title}</title>
      %else:
        <title>Backbone/Pyramid</title>
      %endif
        <link href="//netdna.bootstrapcdn.com/bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet">
        <link href="/root.css"
    </head>
    <body>
        <div id="wrap">
            <div class="container">
                <h1>Backbone/Pyramid</h1>
            </div>
            ${next.body()}
            <div id="push"></div>
        </div>
        <div id="footer">
            <div class="container">
                <p class="pull-left"><strong>A simple project to learn <a href="http://www.pylonsproject.org/">Pyramid</a> and <a href="http://backbonejs.org/">Backbone.js</a>.</strong></p>
                <div class="clearfix"></div>
                <p class="pull-left">by: <a href="https://github.com/adoc/">Nick Long</a> (Jan. 2014)</p>
                <div class="clearfix"></div>
                <p class="pull-left">Inspired by <a href="http://backbonetutorials.com/videos/beginner/">Backbone Tutorials</a> and <a href="http://backbonetutorials.com/organizing-backbone-using-modules/">Organizing Backbone</a></p>
                <div class="clearfix"></div>
                <div class="pull-right">
                    <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a>
                </div>
            </div>
        </div>
        <script src="/lib/require-min.js" type="text/javascript"></script>
        <script src="/common.js" type="text/javascript"></script>
        <script>
            ${next.script()}
        </script>
    </body>
</html> 