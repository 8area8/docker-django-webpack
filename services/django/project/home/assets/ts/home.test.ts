const home = require("./home");

test("testing Home", () => {
    expect(home("foo").greet()).toBe("Hello, foo");
});
