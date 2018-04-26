Git
Воркеры с тегами как в gitlabci.
Матрица свойств как в travis.
Интерполяция любых строк.
Пайплайнов нет. Стадий нет. Степов нет.
Каждая строка в ``script`` запускается в отдельном шелле.
Есть список задач, которые могут выполняться автоматически или
по событию (руками, триггер)
В базу импортится вся история бранчей.

$CINATOR_CONTROL/trigger
$CINATOR_CONTROL/call
$CINATOR_CONTROL/description
$CINATOR_ENV/var1
$CINATOR_ARTIFACTS/some-package.tar.gz
$CINATOR_CHANGES/comment
$CINATOR_CHANGES/files

$CINATOR_TASK_ID
$CINATOR_COMMIT_ID
$CINATOR_COMMIT_NAME
$CINATOR_OWNER
$CINATOR_TAGS


? try как у билдбота.

Таски
=====

Над каждым коммитом (бранчем) можно выполнить таски. Например, test, build, deploy.
Таски могут быть ограничены на запуск. Главный механизм —
привязка групп пользователей к воркерам. Например, есть воркер, который может
деплоить код на прод, на нем могут выполнять таски только админы проекта.

Таски могут вызывать другие таски через trigger/call в yml-config или через
$BLBT_CONTROL/trigger/call. Таски вызываются параллельно (trigger) или
последовательно (call). Максимальная вложенность 10.


Переменные
==========

У каждого джоба есть переменные окружения, env.
Они могут задаваться в yml-конфиге, выбираться руками из UI,
приходить из системных настроек, задаваться через $BLBT_ENV/var,
подтягиваться из родительского джоба, задаваться через параметры
триггера.


.blbt-ci.yml
============

::

    version: 1

    test:
        run: auto
        env:
            PYIMAGE:
                - python-27
                - python-34
                - python-35
                - python-36

        checkout: true
        worker: linux docker
        script:
            - py.test
        on_fail: send-slack-notification.sh $BLBT_STAGE_URL
        branches:
            - master
            - develop

    deploy-stage:
        env:
            HOST:
                - stage1.example.com
                - stage2.example.com
        env-rules:
            HOST:
                input: strict-choice
        checkout: false
        call:
            - name: build
            - name: deploy
              env:
                  PROFILE: staging

    build:
        worker: linux docker
        script:
            - bin/build.sh $BLBT_ARTIFACTS

    deploy:
        worker: linux deploy
        checkout: false
        script:
            - bin/ensure-image $BLBT_ARTIFACTS/app.image
            - bin/deploy $HOST $PROFILE $BLBT_ARTIFACTS/release.tar.gz


Flow
====

* Добавляется проект.
  Имя.
  Ссылка на клонирование.
  GIT_SSH_KEY.
  GIT_SSH_KNOWNHOSTS. (Автозаполняется).
  GIT_USERNAME.
  GIT_PASSSWORD.

* blbt делает клонирование и ищет файл .blbt-ci.yml
