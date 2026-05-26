# Handoff Prompt: Create `.idx` Repository File List

Ты выполняешь простую тестовую задачу в репозитории `C:/Development/upe/UPE`: прочитать структуру репозитория и создать список файлов в папке `.idx`.

## Critical Constraints
- Работай в корне репозитория: `C:/Development/upe/UPE`.
- Не меняй существующие product/source файлы в `docs/`, `prompts/`, `src/`, `.plans/` и `azure-pipelines.yml`.
- Разрешённые изменения для реализации задачи: только создать/обновить файлы внутри `.idx/`.
- Не включай `.git/**` в индекс.
- Не включай `.idx/**` в исходный набор индексируемых файлов, чтобы индекс не ссылался сам на себя как на source input.
- После выполнения пометь выполненные шаги в ответе тегами `[DONE:n]`.

## Codebase Context
Текущий репозиторий — knowledge/materials repo по UPE (Unified Project Execution), в основном Markdown и текстовые документы.

Верхний уровень, найденный на этапе планирования:
- `.git/` — Git metadata, исключить из индекса.
- `.plans/` — planning artifacts; можно включить в индекс как часть репозитория, если не получено другое указание.
- `docs/` — основные документы UPE:
  - `docs/UPE_Executive_Summary_v1.md`
  - `docs/UPE_Functional_Blocks_v1.md`
  - `docs/UPE_Functional_Blocks_v1.pdf`
  - `docs/brainstorming.md`
- `prompts/`:
  - `prompts/LLM-Native Product Design Framework.md`
- `src/`:
  - `src/chat/UPE Platform Architects Chat.md`
  - `src/loop/loop.md`
  - `src/moms/*` meeting notes/transcripts
  - `src/vendors/*` vendor notes
- `azure-pipelines.yml` — pipeline config.

На этапе планирования папки `.idx/` не было.

## Full Plan to Execute

1. Проверь состояние репозитория read-only командами/инструментами: `git status --short`, `ls`, `find`. Убедись, существует ли `.idx/`.
2. Собери список файлов для индексации по правилу:
   - включить обычные файлы репозитория;
   - исключить `.git/**`;
   - исключить `.idx/**`;
   - для теста включить `.plans/**`, если пользователь не попросил исключить planning artifacts.
3. Создай папку `.idx/` в корне репозитория, если её нет.
4. Создай `.idx/files.md` как основной human-readable индекс. Формат:
   ```markdown
   # Repository File Index

   Generated: <ISO или локальная дата-время>

   Scope: all repository files except `.git/**` and `.idx/**`.

   Total files: <N>

   ## Root
   - `azure-pipelines.yml`

   ## .plans
   - `.plans/...`

   ## docs
   - `docs/...`

   ## prompts
   - `prompts/...`

   ## src
   - `src/...`
   ```
   Пути должны быть относительными от корня репозитория и отсортированы по алфавиту.
5. Опционально создай `.idx/files.txt` с тем же списком, по одному относительному пути на строку. Если хочешь сделать задачу максимально минимальной — можно не создавать, но тогда явно укажи это в финальном ответе.
6. Выполни sanity check:
   - прочитай `.idx/files.md`;
   - проверь, что есть ключевые пути: `azure-pipelines.yml`, `docs/UPE_Executive_Summary_v1.md`, `prompts/LLM-Native Product Design Framework.md`, `src/loop/loop.md`;
   - проверь, что нет `.git/HEAD` и нет `.idx/files.md` в списке source files.
7. В финальном ответе по-русски кратко напиши:
   - какие файлы созданы в `.idx/`;
   - сколько файлов проиндексировано;
   - какие исключения применены;
   - теги выполнения `[DONE:1]` ... `[DONE:7]`.

## Gotchas
- В путях есть пробелы и скобки, например `prompts/LLM-Native Product Design Framework.md` и файлы в `src/moms/`. Не ломай такие имена при генерации списка.
- В репозитории нет `.gitignore`, поэтому не полагайся только на ignore rules; явно исключай `.git` и `.idx`.
- Не нужно читать или парсить PDF/большие transcript файлы — задача только про список путей.
- Если используешь shell, аккуратно обрабатывай имена с пробелами; лучше использовать `find` с сортировкой или скрипт, который корректно работает с путями.
