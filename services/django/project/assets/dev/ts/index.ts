// Main javascript file. Entry for Webpack.

// SCSS importations
import "../../../home/assets/scss/main.scss";
import "../scss/index.scss";

// Typescript importations
import { setupDom as homeSetup } from "../../../home/assets/ts/main";

document.addEventListener("DOMContentLoaded", () => {
    // Main function.
    const page = window.location.pathname;

    switch (page) {
        case "/": {
            homeSetup();
            break;
        }
    }

}, false);
