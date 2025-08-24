const { execSync } = require("child_process");
const fs = require("fs");

const targetPorts = [3000]; // change or add more ports if needed

const getProcesses = () => {
  try {
    const output = execSync("lsof -iTCP -sTCP:LISTEN -n -P").toString();
    const lines = output.split("\n").slice(1); // skip header

    const processes = [];

    lines.forEach(line => {
      const columns = line.trim().split(/\s+/);
      const command = columns[0];
      const pid = columns[1];
      const portMatch = line.match(/:(\d+)\s/);

      if (portMatch && targetPorts.includes(Number(portMatch[1]))) {
        let path = "N/A";
        try {
          path = fs.readlinkSync(`/proc/${pid}/cwd`);
        } catch {
          // macOS fallback
          try {
            const cmdOut = execSync(`lsof -p ${pid} | grep cwd`).toString();
            path = cmdOut.split(/\s+/).pop();
          } catch {
            path = "Could not determine path";
          }
        }

        processes.push({
          port: portMatch[1],
          pid,
          command,
          path,
        });
      }
    });

    return processes;
  } catch (e) {
    console.error("Error checking ports:", e.message);
    return [];
  }
};

const results = getProcesses();
if (results.length === 0) {
  console.log("✅ Port 3000 is free!");
} else {
  console.log("🚫 Port 3000 is already in use by:");
  results.forEach(proc => {
    console.log(`\n🔌 Port: ${proc.port}\n⚙️ PID: ${proc.pid}\n📁 Path: ${proc.path}\n🔧 Command: ${proc.command}`);
  });
}
