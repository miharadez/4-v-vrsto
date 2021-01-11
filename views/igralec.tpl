<html>
    <head>
        <title>{{ime}}, 4 v vrsto posebej zate</title>
    </head>
    <body>
        <b>Želiš začeti (boš igralec 1) ali daš prednost nasprotniku (boš igralec 2)</b>
        % a = ["1", "2"]
        % for igralec in a:
        <form action="/{{ime}}/{{level}}/{{igralec}}/" method="post">
            <input type="submit" value="{{igralec}}">
        </form>
        %end
    </body>

</html>