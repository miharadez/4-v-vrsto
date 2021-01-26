<html>
    <head>
        <title>Zmaga!</title>
    </head>
    <style>
    h2 {text-align: center;}
    </style>
    <body>
        <h2>Zaslužena zmaga! Bravo {{ime}}!</h2>
        % import html
        % a = list(tabela)
        % for vrstica in tabela:
        % vr = str(vrstica)
        % v = html.unescape(vr)
        <h2>{{v}}</h2>
        % end
        Si upate preizkusiti še kakšen drug level?
        <form action="/{{ime}}/" method="post">
            <input type="submit" value="Sprejmem iziv!">
        </form>
    </body>
</html>