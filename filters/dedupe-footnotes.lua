-- Pandoc makes a new numbered Note for every [^n] reference, so a source cited
-- twice appeared twice in the notes list, renumbered. Keep the first Note for
-- each content and point later repeats at it with Quarto's own noteref markup,
-- so the hover tooltip (which follows href) still works. Kept notes stay in
-- first-appearance order, which is the order the HTML writer numbers them in.
local seen, count, repeats = {}, 0, {}

function Note(note)
  if not FORMAT:match('html') then return nil end
  local key = pandoc.write(pandoc.Pandoc(note.content), 'native')
  local n = seen[key]
  if not n then
    count = count + 1
    seen[key] = count
    return nil
  end
  repeats[n] = (repeats[n] or 1) + 1
  return pandoc.RawInline('html', string.format(
    '<a href="#fn%d" class="footnote-ref" id="fnref%d-%d" role="doc-noteref"><sup>%d</sup></a>',
    n, n, repeats[n], n))
end
