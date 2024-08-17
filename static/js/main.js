var auxBack = performance.getEntriesByType("navigation");

if (auxBack[0].type === "back_forward") {
    location.reload(true);
}