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
