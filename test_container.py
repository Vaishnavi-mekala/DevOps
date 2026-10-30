const { Builder, By } = require("selenium-webdriver");
const chrome = require("selenium-webdriver/chrome");
const assert = require("assert");

async function testApplication() {

    const options = new chrome.Options();
    options.addArguments("--headless", "--no-sandbox");

    const driver = await new Builder()
        .forBrowser("chrome")
        .setChromeOptions(options)
        .build();

    try {

        // Test 1: Verify page title
        await driver.get("http://localhost:8081");

        const title = await driver.getTitle();

        assert.strictEqual(title, "JavaScript Application");

        console.log("Test Case 1 Passed: Page title verified");


        // Test 2: Verify heading
        const heading =
            await driver.findElement(By.tagName("h1")).getText();

        assert.strictEqual(heading, "Simple JavaScript Program");

        console.log("Test Case 2 Passed: Heading verified");


        // Test 3: Verify addition functionality
        await driver.findElement(By.id("num1")).sendKeys("10");

        await driver.findElement(By.id("num2")).sendKeys("20");

        await driver.findElement(By.id("addBtn")).click();

        const result =
            await driver.findElement(By.id("result")).getText();

        assert.strictEqual(result, "Result: 30");

        console.log("Test Case 3 Passed: Addition verified");


        // Test 4: Verify another calculation
        await driver.findElement(By.id("num1")).clear();

        await driver.findElement(By.id("num2")).clear();

        await driver.findElement(By.id("num1")).sendKeys("5");

        await driver.findElement(By.id("num2")).sendKeys("7");

        await driver.findElement(By.id("addBtn")).click();

        const secondResult =
            await driver.findElement(By.id("result")).getText();

        assert.strictEqual(secondResult, "Result: 12");

        console.log("Test Case 4 Passed: Second calculation verified");

    } finally {
        await driver.quit();
    }
}

testApplication().catch(error => {
    console.error("Test failed:", error);
    process.exitCode = 1;
});