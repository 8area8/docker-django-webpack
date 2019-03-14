// Jest example.

import { Home } from "../home";

test("testing Home", () => {
    const foo = new Home("foo");
    expect(foo.greet()).toBe("Hello, foo");
});
