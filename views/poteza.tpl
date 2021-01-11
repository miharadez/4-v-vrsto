<html>
    <head>
        <title>{{ime}}, 4 v vrsto posebej zate</title>
    </head>
    <body>
        <b>Izberi željeni stolpec</b>
        % a = list(tabela)
        % for vrstica in tabela:
        <h2>{{vrstica}}</h2>
        % end
        <h2>|_1_|_2_|_3_|_4_|_5_|_6_|_7_|</h2>
        % op = list(opcije)
        % for opcija in op:
        % vrednost = opcija + 1
        <form action="/{{ime}}/{{level}}/{{igralec}}/{{opcija}}/" method="post">
            <input type="submit" value="{{vrednost}}">
        </form>
    </body>
</html>