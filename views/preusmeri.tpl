<html>
    <head>
        <title>Preusmeritev na lastno stran</title>
    </head>
    <body>
        <h2>Izbrali ste ime {{ ime }}</h2>
        <form action="/{{ime}}/" method="post">
            <input type="submit" value="Naprej">
        </form>
    </body>
</html>