from cinator.source import git


def get_refs():
    source = git.Git('/home/bobrov/work/covador', '/tmp/repo')
    refs = source.get_refs()
    commit_ids = set(r[0] for r in refs)
    info = source.get_info(commit_ids)
    result = []
    for cid, name in refs:
        info[cid]['name'] = name
        result.append(info[cid].copy())
    return result
