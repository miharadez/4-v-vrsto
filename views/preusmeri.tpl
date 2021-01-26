<html>
    <head>
        <title>Preusmeritev na lastno stran</title>
    </head>
    <body>
        <h2>Ime ti je {{ ime }}</h2>
        <form action="/{{ime}}/" method="post">
            <input type="submit" value="Naprej">
        </form>
    </body>
</html>