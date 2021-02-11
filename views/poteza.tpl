<html>
<style>
form {display: inline-block; form-align: center;}
h2 {text-align: center;}
.buttonHolder { text-align: center; }
</style>
    <head>
        <title>{{ime}}, 4 v vrsto posebej zate</title>
    </head>
    <body>
        <h2>Izberi željeni stolpec</h2>
        % import html
        % a = list(tabela)
        % for vrstica in tabela:
        % vr = str(vrstica)
        % v = html.unescape(vr)
        <h2>{{v}}</h2>
        % end
        <div class="buttonHolder">
            &#160;
            <form action="/{{ime}}/{{level}}/{{igralec}}/{{0}}/" method="post">
                <input type="submit" value="1">
            </form>
            &#160;&#160;&#160;&#160;&#160;
            <form action="/{{ime}}/{{level}}/{{igralec}}/{{1}}/" method="post">
                <input type="submit" value="2">
            </form> 
            &#160;&#160;&#160;&#160;&#160;
            <form action="/{{ime}}/{{level}}/{{igralec}}/{{2}}/" method="post">
                <input type="submit" value="3">
            </form>
            &#160;&#160;&#160;&#160;&#160;
            <form action="/{{ime}}/{{level}}/{{igralec}}/{{3}}/" method="post">
                <input type="submit" value="4">
            </form>
            &#160;&#160;&#160;&#160;&#160;
            <form action="/{{ime}}/{{level}}/{{igralec}}/{{4}}/" method="post">
                <input type="submit" value="5">
            </form>
            &#160;&#160;&#160;&#160;&#160;
            <form action="/{{ime}}/{{level}}/{{igralec}}/{{5}}/" method="post">
                <input type="submit" value="6">
            </form>
            &#160;&#160;&#160;&#160;&#160;
            <form action="/{{ime}}/{{level}}/{{igralec}}/{{6}}/" method="post">
                <input type="submit" value="7">
            </form>
            &#160;&#160;&#160;&#160;&#160;
        </div>
    </body>
</html>