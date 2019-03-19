// Home ts from 'home' app.

export class Home {
    // Home class.

    private greeting: string;

    constructor(message: string) {
        // Init function.
        this.greeting = message;
    }

    public greet() {
        return "Hello, " + this.greeting;
    }
}

export function setupDom(): void {
    // Set up all DOM elements.
    const button: HTMLElement | null = document.getElementById("selenium-test");

    if (button) {
        button.addEventListener("click", function(event) {
            const style: CSSStyleDeclaration = this.style;

            if (this.classList.contains("colored")) {
                style.color = "black";
                style.backgroundColor = "white";
                this.classList.remove("colored");
                return;
            }
            style.color = "blue";
            style.backgroundColor = "black";
            this.classList.add("colored");
        });
    } else {
        throw new TypeError("#selenium-test is undefined.");
    }
}
