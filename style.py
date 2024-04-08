body {
    font-family: Arial,  sans-serif; /* Семейство шрифтов */
    font-size: 11px; /* Размер основного шрифта в <p></p>  */
    background-color: #17ebe7; /* Цвет фона веб-страницы */
    color: #333333; /* Цвет основного текста */ 
}
h1 {
    color: #00a800; /* Цвет заголовка */
    font-size: 24px; /* Размер шрифта в пунктах */
    font-family: Georgia, serif; /* Семейство шрифтов */
}
@keyframes color-change {
    0% {
      color: blue;
    }
  
    50% {
      color: red;
    }
  
    100% {
      color: rgb(0, 170, 255);
    }
}

h1:hover{
    animation: color-change 3s infinite;
} 
