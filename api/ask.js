// Vercel serverless function (runs alongside the static Astro build via the
// root /api dir — no SSR adapter needed). Receives an inline-submitted question
// and files it as a GitHub issue for review. No DB, no submitter account.
//
// Requires env var AC_GUIDE_GH_TOKEN: a fine-grained PAT with Issues: read/write
// on wilsonpruitt/ac-guide. Set it in Vercel (Production + Preview).

const REPO = 'wilsonpruitt/ac-guide';

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed.' });
  }
  const token = process.env.AC_GUIDE_GH_TOKEN;
  if (!token) {
    return res.status(500).json({ error: 'Question intake isn’t configured yet.' });
  }

  let body = req.body;
  if (typeof body === 'string') {
    try { body = JSON.parse(body); } catch { body = {}; }
  }
  const { ref = '', question = '', name = '', page = '', website = '' } = body || {};

  // Honeypot — bots fill hidden fields; humans don't. Pretend success.
  if (website) return res.status(200).json({ ok: true });

  const q = String(question).trim();
  if (q.length < 5 || q.length > 1000) {
    return res.status(400).json({ error: 'A question should be between 5 and 1000 characters.' });
  }
  const safeRef = String(ref).slice(0, 120);
  const safePage = String(page).slice(0, 200);
  const safeName = String(name).trim().slice(0, 80);

  const title = `Question: ${q.slice(0, 70)}${q.length > 70 ? '…' : ''}`;
  const issueBody = [
    q,
    '',
    `**Target:** \`${safeRef || '(unspecified)'}\``,
    safePage ? `**Page:** ${safePage}` : '',
    safeName ? `**Asked by:** ${safeName}` : '_Asked anonymously._',
    '',
    '_Submitted via the Guide to Annual Conference “Ask about this” widget._',
  ].filter(Boolean).join('\n');

  try {
    const r = await fetch(`https://api.github.com/repos/${REPO}/issues`, {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${token}`,
        Accept: 'application/vnd.github+json',
        'Content-Type': 'application/json',
        'User-Agent': 'ac-guide-ask',
      },
      body: JSON.stringify({ title, body: issueBody, labels: ['question'] }),
    });
    if (!r.ok) {
      return res.status(502).json({ error: 'Couldn’t file the question right now. Please try again later.' });
    }
    return res.status(200).json({ ok: true });
  } catch {
    return res.status(502).json({ error: 'Couldn’t reach the question intake. Please try again later.' });
  }
}
