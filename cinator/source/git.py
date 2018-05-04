import os.path
from subprocess import check_output, check_call, run, PIPE


class Git:
    def __init__(self, url, workdir=None):
        self.url = url
        self.workdir = workdir
        if workdir:
            self.ensure_workdir()

    def ensure_workdir(self):
        os.makedirs(self.workdir, exist_ok=True)
        if not os.path.exists(os.path.join(self.workdir, '.git')):
            check_call(['git', 'init'], cwd=self.workdir)

    def get_refs(self):
        out = check_output(['git', 'ls-remote', '--quiet', '--heads', '--tags', self.url])
        result = []
        for r in out.splitlines():
            cid, name, *rest = r.split(b'\t')
            result.append((cid.decode(), name.decode()))

        commit_ids = set(r[0] for r in result)
        check_output(['git', 'fetch', '--quiet', '--depth=1', self.url, *commit_ids],
                     cwd=self.workdir)

        return result

    def get_info(self, commit_ids):
        out = check_output(['git', 'show', '--quiet',
                            '--format=format:%H\t%an\t%ae\t%ct\t%s', *commit_ids],
                           cwd=self.workdir)

        result = {}
        for line in out.splitlines():
            commit_id, author, email, ts, message = line.split(b'\t')
            commit_id = commit_id.decode()
            result[commit_id] = {
                'commit_id': commit_id,
                'author': author.decode().strip(),
                'email': email.decode().strip(),
                'date': int(ts.decode()),
                'message': message.decode().strip(),
            }

        return result
