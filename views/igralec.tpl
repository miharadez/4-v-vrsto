<html>
    <head>
        <title>{{ime}}, 4 v vrsto posebej zate</title>
    </head>
    <body>
        <b>Boš igralec 1(&#128308;) ali 2(&#128309;)?</b>
        % a = ["1", "2"]
        % for igralec in a:
        <form action="/{{ime}}/{{level}}/{{igralec}}/" method="post">
            <input type="submit" value="{{igralec}}">
        </form>
        %end
    </body>

</html>