// Jest example.

import { Home } from "../home";

describe("Testing Home object.", () => {

    describe("Testing greet method.", () => {

        it("greet method return 'Hello, foo'.", () => {
            const foo = new Home("foo");
            expect(foo.greet()).toBe("Hello, foo");
        });
    });
});
