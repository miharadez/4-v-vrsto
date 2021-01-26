<html>
    <head>
        <title>{{ime}}, 4 v vrsto posebej zate</title>
    </head>
    <style>
    h2 {text-align: center;}
    </style>
    <body>
        <h2>Izberi željeni stolpec</h2>
        % import html
        % a = list(tabela)
        % for vrstica in tabela:
        % vr = str(vrstica)
        % v = html.unescape(vr)
        <h2>{{v}}</h2>
        % end
        % op = list(opcije)
        % for opcija in op:
        % vrednost = opcija + 1
        <div class="name">
        <form action="/{{ime}}/{{level}}/{{igralec}}/{{opcija}}/" method="post">
            <input type="submit" value="{{vrednost}}">
        </form>
        % end
        </div>
    </body>
</html>