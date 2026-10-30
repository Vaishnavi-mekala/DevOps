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
        await driver.get(
            "file://" + process.cwd() + "/index.html"
        );

        
        const title = await driver.getTitle();

        assert.strictEqual(title, "JavaScript Application");

        console.log("Test 1 Passed: Page title verified");

       
        await driver.findElement(By.id("num1")).sendKeys("10");
        await driver.findElement(By.id("num2")).sendKeys("20");

        await driver.findElement(By.id("addBtn")).click();

        const result =
            await driver.findElement(By.id("result")).getText();

        assert.strictEqual(result, "Result: 30");

        console.log("Test 2 Passed: Addition verified");

    } finally {
        await driver.quit();
    }
}

testApplication().catch(error => {
    console.error(error);
    process.exitCode = 1;
});
