import type { LayoutServerLoad } from "./$types";

export const load = (async ({ url }) => {
  return {
    computedUrl: `${url.origin}${url.pathname}`,
  };
}) satisfies LayoutServerLoad;
