<html>
    <head>
        <title>Poraz</title>
    </head>
    <body>
        <h2>Ne jokaj {{ime}}, morda ti uspe v naslednjem poizkusu.</h2>
        % import html
        % a = list(tabela)
        % for vrstica in tabela:
        % vr = str(vrstica)
        % v = html.unescape(vr)
        <h2>{{v}}</h2>
        % end
        <h2>|_1_|_2_|_3_|_4_|_5_|_6_|_7_|</h2>
        <form action="/{{ime}}/" method="post">
            <input type="submit" value="Revanša!">
        </form>
    </body>
</html>