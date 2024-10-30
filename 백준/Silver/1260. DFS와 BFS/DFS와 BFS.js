const input = require("fs")
  .readFileSync("./dev/stdin")
  .toString()
  .trim()
  .split("\n");

const [n, _, v] = input.shift().split(" ").map(Number);
const edges = input.map((v) => v.split(" ").map(Number));

let graph = Array.from({ length: n + 1 }, () =>
  Array.from({ length: n + 1 }).fill(0)
);

edges.forEach(([a, b]) => {
  graph[a][b] = 1;
  graph[b][a] = 1;
});

let visited_dfs = Array.from({ length: n + 1 }).fill(0);
let visited_bfs = Array.from({ length: n + 1 }).fill(0);

dfs(v);
console.log("");
bfs(v);

function dfs(v) {
  visited_dfs[v] = 1;
  process.stdout.write(v + " ");
  for (let i = 1; i <= n; i++) {
    if (graph[v][i] === 1 && visited_dfs[i] === 0) {
      dfs(i);
    }
  }
}
function bfs(v) {
  let queue = [v];
  visited_bfs[v] = 1;
  while (queue.length > 0) {
    v = queue.shift();
    process.stdout.write(v + " ");
    for (let i = 1; i <= n; i++) {
      if (graph[v][i] === 1 && visited_bfs[i] === 0) {
        queue.push(i);
        visited_bfs[i] = 1;
      }
    }
  }
}
