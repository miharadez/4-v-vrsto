<html>
    <head>
        <title>{{ime}}, 4 v vrsto posebej zate</title>
    </head>
    <style>
    h2 {text-align: center;}
    </style>
    <body>
        <h2>Izenačenje!</h2>
        <h2>{{ime}}, dobro si se boril.</h2>
        % import html
        % a = list(tabela)
        % for vrstica in tabela:
        % vr = str(vrstica)
        % v = html.unescape(vr)
        <h2>{{v}}</h2>
        % end
        Si želite poizkusiti še enkrat?
        <form action="/{{ime}}/" method="post">
            <input type="submit" value="Sprejmem iziv!">
        </form>
    </body>
</html>