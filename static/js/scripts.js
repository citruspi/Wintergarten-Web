(function () {

    switch (window.location.pathname.split('/')[1]) {

        case 'top':

            document.getElementById("top").style.textDecoration="underline";
            break;

        case 'theatres':

            document.getElementById("theatres").style.textDecoration="underline";
            break;

        case 'upcoming':

            document.getElementById("upcoming").style.textDecoration="underline";
            break;

        case 'search':

            document.getElementById("search").style.textDecoration="underline";
            break;        

        default:

            document.getElementById("search").style.textDecoration="underline";

    }

})();

(function () {
    
    document.getElementById("submit").addEventListener("click", function () {

        document.getElementById("search_form").submit();

    }, false);

})();
