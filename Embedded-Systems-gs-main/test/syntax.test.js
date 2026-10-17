const { test } = require("node:test");
const assert = require("node:assert");
const { execFileSync } = require("node:child_process");
const path = require("node:path");

const root = path.join(__dirname, "..");
const files = [
  "control-unit-iot.js",
  "sender.js",
  "test-mqtt.js",
  "test-serial.js",
];

for (const file of files) {
  test(`${file} has valid syntax`, () => {
    assert.doesNotThrow(() =>
      execFileSync(process.execPath, ["--check", path.join(root, file)]),
    );
  });
}

test("required dependencies are installed", () => {
  for (const dep of ["express", "mqtt", "cors", "serialport"]) {
    assert.ok(require.resolve(dep, { paths: [root] }));
  }
});
