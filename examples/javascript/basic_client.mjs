const BASE_URL = process.env.BASE_URL || "https://sandbox.api.neurocad.eu";

async function issueToken() {
  const response = await fetch(`${BASE_URL}/v1/auth/token`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      client_id: "partner_demo",
      client_secret: "replace-in-production",
      audience: "enterprise-api",
    }),
  });

  return response.json();
}

async function submitJob(token, projectId) {
  const response = await fetch(`${BASE_URL}/v1/inference/jobs`, {
    method: "POST",
    headers: {
      Authorization: `Bearer ${token}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      project_id: projectId,
      task: "mesh-generation",
      input: {
        material: "steel-a36",
        resolution: "medium",
      },
      labels: ["js-example"],
    }),
  });

  return response.json();
}

async function main() {
  console.log("Draft public example. Replace placeholder credentials before use.");
  const tokenResponse = await issueToken();
  const result = await submitJob(tokenResponse.access_token, "prj_demo_001");
  console.log(JSON.stringify(result, null, 2));
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
