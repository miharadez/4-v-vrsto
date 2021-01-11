<html>
    <head>
        <title>{{ime}}, 4 v vrsto posebej zate</title>
    </head>
    <body>
        <h2>Živjo, {{ime}}!</h2>
        <b>Izberi željeno težavnost.</b>

        % a = ["zelo lahko", "lahko", "srednje", "težje", "težko"]
        % for level in a:
        <li>
        {{level}}
        <form action="/{{ime}}/{{level}}/" method="post">
            <input type="submit" value="izberi">
        </form>
        </li>
        %end
    </body>

</html>