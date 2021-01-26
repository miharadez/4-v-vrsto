<html>
    <head>
        <title>Poraz</title>
    </head>
    <style>
    h2 {text-align: center;}
    </style>
    <body>
        <h2>Ne jokaj {{ime}}, morda ti uspe v naslednjem poizkusu.</h2>
        % import html
        % a = list(tabela)
        % for vrstica in tabela:
        % vr = str(vrstica)
        % v = html.unescape(vr)
        <h2>{{v}}</h2>
        % end
        <form action="/{{ime}}/" method="post">
            <input type="submit" value="Revanša!">
        </form>
    </body>
</html>